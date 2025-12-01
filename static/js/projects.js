/* =====================================================
   📌 ANIMATE PROJECT CARDS ON SCROLL
===================================================== */
const cards = document.querySelectorAll('.project-card');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.2 });

cards.forEach(card => observer.observe(card));


/* =====================================================
   📌 TAB SWITCHING FOR FORMS
===================================================== */
const tabs = document.querySelectorAll('.tab');
const contents = document.querySelectorAll('.form-content');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.remove('active'));
    contents.forEach(c => c.classList.remove('active'));

    tab.classList.add('active');
    document.getElementById(tab.dataset.target).classList.add('active');
  });
});


/* =====================================================
   📌 UNIVERSAL BACKEND FORM SENDER
===================================================== */
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
      alert("Failed to send form. Try again.");
  }
}


/* =====================================================
   🔵 NEW PROJECT SUBMISSION (Projects Page)
===================================================== */
document.addEventListener("DOMContentLoaded", () => {
  const newProjectForm = document.getElementById("newProjectForm");

  if (newProjectForm) {
      newProjectForm.addEventListener("submit", function(e) {
          e.preventDefault();
          sendForm("/send_new_project", this);  
      });
  }
});


/* =====================================================
   🟡 PARTNER WITH PROJECT FORM
===================================================== */
document.addEventListener("DOMContentLoaded", () => {
  const partnerProjectForm = document.getElementById("partnerProjectForm");

  if (partnerProjectForm) {
      partnerProjectForm.addEventListener("submit", function(e) {
          e.preventDefault();
          sendForm("/send_partner_project", this);
      });
  }
});


fetch("/send_project_submission", {
    method: "POST",
    body: new FormData(this)
});

fetch("/send_project_partner", {
    method: "POST",
    body: new FormData(this)
});
