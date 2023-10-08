document.querySelector("#signin-form").addEventListener("submit", function(event) {
    event.preventDefault();
  
    // Get the selected radio button
    const selectedRadio = document.querySelector('input[name="role"]:checked');
  
    // Redirect the user to the appropriate page
    if (selectedRadio.value === "admin") {
      window.location.href = "admin.html";
    } else if (selectedRadio.value === "patient") {
      window.location.href = "patient.html";
    }
  });
  