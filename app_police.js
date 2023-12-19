// app_police.js
function login() {
    const aadharNumber = prompt('Enter Aadhar Number:');
  
    if (aadharNumber) {
      // Simulate authentication, in a real system this would involve server-side validation
      loggedInUser = {
        type: 'police',
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
  
  function sendNotification() {
    alert('Notification sent to camera owners and law enforcement about suspicious activity.');
  }
  