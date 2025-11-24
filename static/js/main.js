document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("contactForm");

  // Make sure the form exists
  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault(); // stop default form submission

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
      // Send data as JSON to Flask
      const response = await fetch("/subscribe", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        alert("✅ Thank you! Your message has been sent successfully.");
        form.reset();
      } else {
        alert("⚠️ Something went wrong. Please try again later.");
      }
    } catch (error) {
      console.error("Error submitting form:", error);
      alert("⚠️ Network error. Please check your connection.");
    }
  });
});
document.addEventListener("mousemove", (e) => {
  const logo = document.querySelector(".site-header .logo");
  if (!logo) return;

  const x = e.clientX;
  const y = e.clientY;
  const rect = logo.getBoundingClientRect();
  const offsetX = x - (rect.left + rect.width / 2);
  const offsetY = y - (rect.top + rect.height / 2);

  logo.style.transform = `scale(1.15) rotate(${offsetX / 20}deg)`;
  logo.style.filter = `drop-shadow(${offsetX / 10}px ${offsetY / 10}px 20px #00ff88) drop-shadow(${-offsetX / 10}px ${-offsetY / 10}px 25px #6a00ff)`;
});

/* ================================
   📌 UNIVERSAL FORM SENDER FUNCTION
================================= */
async function sendForm(endpoint, formElement) {
    const formData = new FormData(formElement);

    try {
        const response = await fetch(endpoint, {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        alert(result.message);
        if (response.ok) formElement.reset();
    } catch (error) {
        alert("Failed to send form. Check your internet and try again.");
    }
}

/* ================================
   🟡 PARTNERSHIP FORM (FUTURE PAGE)
================================= */
document.addEventListener("DOMContentLoaded", () => {
    const partnerForm = document.getElementById("partnerForm");
    if (partnerForm) {
        partnerForm.addEventListener("submit", function(e) {
            e.preventDefault();
            sendForm("/send_partner", this);
        });
    }
});

/* ===========================================
   🟢 BOARD OF GOVERNORS FORM (ABOUT PAGE)
=========================================== */
document.addEventListener("DOMContentLoaded", () => {
    const boardForm = document.getElementById("boardForm");
    if (boardForm) {
        boardForm.addEventListener("submit", function(e) {
            e.preventDefault();
            sendForm("/send_board_application", this);
        });
    }
});

/* =====================================
   🔵 EMPLOYEE APPLICATION FORM (ABOUT)
===================================== */
document.addEventListener("DOMContentLoaded", () => {
    const employeeForm = document.getElementById("employeeForm");
    if (employeeForm) {
        employeeForm.addEventListener("submit", function(e) {
            e.preventDefault();
            sendForm("/send_employee_application", this);
        });
    }
});

/* =====================================
   🔴 MEMBER REGISTRATION FORM (HOME)
===================================== */
document.addEventListener("DOMContentLoaded", () => {
    const memberForm = document.getElementById("memberForm");
    if (memberForm) {
        memberForm.addEventListener("submit", function(e) {
            e.preventDefault();
            sendForm("/send_member", this);
        });
    }
});
