// Animate cards on scroll
const cards = document.querySelectorAll('.project-card');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.2 });

cards.forEach(card => observer.observe(card));

// Tabs for form switching
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

// Form actions
document.getElementById('newProjectForm').addEventListener('submit', e => {
  e.preventDefault();
  alert('Thank you for your new project submission! YCA team will review it soon.');
  e.target.reset();
});

document.getElementById('partnerProjectForm').addEventListener('submit', e => {
  e.preventDefault();
  alert('Thank you for your willingness to partner with YCA. We’ll reach out shortly.');
  e.target.reset();
});
