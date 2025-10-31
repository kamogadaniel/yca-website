document.getElementById("partnerForm").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const reason = document.getElementById("reason").value;
    const amount = document.getElementById("amount").value;
  
    alert(`Thank you ${name}! Your partnership request has been received. We will contact you via ${email}.`);
    
    // Later, we’ll connect this to your WhatsApp and email backend.
    this.reset();
  });
  