// app_camera_owner.js
function login() {
    const aadharNumber = prompt('Enter Aadhar Number:');
  
    if (aadharNumber) {
      // Simulate authentication, in a real system this would involve server-side validation
      loggedInUser = {
        type: 'cameraOwner',
        aadharNumber,
      };
  
      alert('Login successful!');
      showUserInterface();
    } else {
      alert('Aadhar Number is required.');
    }
  }
  
  function logout() {
    loggedInUser = null;
    alert('Logout successful!');
    showUserInterface();
  }
  
  function activateNoHomeMode() {
    alert('No Home Mode activated. Cameras accessible for a specified duration.');
  }
  