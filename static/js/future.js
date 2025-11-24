// 🔵 FUTURE PARTNERSHIP FORM → SEND TO EMAIL BACKEND
document.addEventListener("DOMContentLoaded", () => {
    const partnerForm = document.getElementById("partnerForm");

    if (partnerForm) {
        partnerForm.addEventListener("submit", async function (e) {
            e.preventDefault();

            const formData = new FormData(this);

            try {
                const response = await fetch("/send_email", {
                    method: "POST",
                    body: formData
                });

                const result = await response.json();
                alert(result.message);

                if (response.ok) this.reset();

            } catch (error) {
                alert("Failed to send. Please try again.");
            }
        });
    }
});
