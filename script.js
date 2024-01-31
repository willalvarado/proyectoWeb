document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("login-form").addEventListener("submit", function(event) {
      event.preventDefault(); // Evitar que el formulario se envíe automáticamente
  
      // Obtener los valores del nombre de usuario y la contraseña
      var username = document.getElementById("username").value;
      var password = document.getElementById("password").value;
  
      // Aquí puedes hacer una solicitud al servidor para verificar las credenciales
      // Por ejemplo, puedes utilizar AJAX para enviar los datos al backend y esperar una respuesta
  
      // Ejemplo de verificación de credenciales (solo para propósitos demostrativos)
      if (username === "william.alvarado@epn.edu.ec" && password === "12345") {
        // Redirigir al usuario a la página deseada después del inicio de sesión exitoso
        window.location.href = "compra.html";
      } else {
        // Mostrar un mensaje de error si las credenciales son incorrectas
        document.getElementById("error-msg").innerText = "Usuario o contraseña incorrectos";
      }
    });
  });
  