// app.js
function showUserInterface() {
    const userTypeSelect = document.getElementById('userType');
    const userInterfaceDiv = document.getElementById('userInterface');
  
    userInterfaceDiv.innerHTML = '';
  
    if (userTypeSelect.value === 'police') {
      userInterfaceDiv.innerHTML = '<object type="text/html" data="police_interface.html"></object>';
      
      <div>
          <h2>Police Interface</h2>
          <button onclick="login()">Login</button>
          <button onclick="logout()">Logout</button>
          <button onclick="sendNotification()">Send Notification</button>
        </div>
        
      const script = document.createElement('script');
      script.src = 'app_police.js';
      document.head.appendChild(script);
    } else if (userTypeSelect.value === 'cameraOwner') {
      userInterfaceDiv.innerHTML = '<object type="text/html" data="camera_owner_interface.html"></object>';
      <div>
      <h2>Camera Owner Interface</h2>
      <button onclick="login()">Login</button>
      <button onclick="logout()">Logout</button>
      <button onclick="activateNoHomeMode()">Activate No Home Mode</button>
    </div>
      const script = document.createElement('script');
      script.src = 'app_camera_owner.js';
      document.head.appendChild(script);
    }
  }
  