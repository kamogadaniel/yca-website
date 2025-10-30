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
