// Sample data simulation
let loggedInUser = null;

function showUserInterface() {
  const userTypeSelect = document.getElementById('userType');
  const userInterfaceDiv = document.getElementById('userInterface');

  userInterfaceDiv.innerHTML = '';

  if (userTypeSelect.value === 'police') {
    userInterfaceDiv.innerHTML = policeInterfaceHTML;
  } else if (userTypeSelect.value === 'cameraOwner') {
    userInterfaceDiv.innerHTML = cameraOwnerInterfaceHTML;
  }
}

function login() {
  const aadharNumber = prompt('Enter Aadhar Number:');

  if (aadharNumber) {
    // Simulate authentication, in a real system this would involve server-side validation
    loggedInUser = {
      type: document.getElementById('userType').value,
      aadharNumber,
    };

    alert('Login successful!');

    // Redirect to the respective portal after login
    if (loggedInUser.type === 'police') {
      redirectToPolicePortal();
    } else if (loggedInUser.type === 'cameraOwner') {
      redirectToCameraOwnerPortal();
    }
  } else {
    alert('Aadhar Number is required.');
  }
}

function logout() {
  loggedInUser = null;
  alert('Logout successful!');
  showUserInterface();
}

function redirectToPolicePortal() {
  // Add logic to redirect to the police portal (e.g., navigate to a different HTML page)
  window.location.href = 'police_front.html';
}

function redirectToCameraOwnerPortal() {
  // Add logic to redirect to the camera owner portal (e.g., navigate to a different HTML page)
  window.location.href = 'owner_front.html';
}

// raj.js
// Sample data simulation for police and camera owner interfaces
const policeInterfaceHTML = `
  <h2>Police Interface</h2>
  <button onclick="login()">Login</button>
  <button onclick="logout()">Logout</button>
  <button onclick="sendNotification()">Send Notification</button>
`;

const cameraOwnerInterfaceHTML = `
  <h2>Camera Owner Interface</h2>
  <button onclick="login()">Login</button>
  <button onclick="logout()">Logout</button>
  <button onclick="activateNoHomeMode()">Activate No Home Mode</button>
`;

function sendNotification() {
  const cameraSerialNumber = prompt('Enter Camera Serial Number:');
  if (cameraSerialNumber) {
    alert(`Notification sent for camera with serial number ${cameraSerialNumber}.`);
  } else {
    alert('Camera Serial Number is required.');
  }
}

function activateNoHomeMode() {
  alert('No Home Mode activated. Cameras accessible for a specified duration.');
}

