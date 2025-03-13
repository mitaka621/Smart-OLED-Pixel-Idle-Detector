<h1>🖥️ OLED Screen Saver</h1>
<h2>💡 Why This is Better Than Windows' Built-in Sleep/Screen Off Function</h2>
<ul>
   <li><strong>Perfect for Watching Movies:</strong> Unlike idle timers, this detects actual screen changes, so it won't turn off while watching videos.</li>
    <li><strong>Customizable Detection:</strong> You can adjust the time before turning off by changing the constants.</li>       
    <li><strong>Extends OLED Lifespan:</strong> Specifically designed to prevent OLED burn-in, unlike Windows' generic sleep function.</li>
</ul>
<h2>🚀 Features</h2>
<ul>
    <li>Monitors pixel changes on the screen.</li>
    <li>Turns off the monitor if no changes occur for a set time.</li>
    <li>Wakes up on mouse movement or keyboard input.</li>
    <li>Runs in the background efficiently.</li>
</ul>   
<h2>⚙️ Requirements</h2>
<p>Ensure you have the following installed:</p>
<pre>pip install mss pillow numpy</pre>
<h2>🔧 Configuration</h2>
<p>You can configure the behavior of the script by modifying the following constants in the <code>main.py</code> file:</p>
<ul>
    <li><code>DEBUG</code>: When set to <code>True</code>, screenshots containing only the pixels which changed between captures will be saved in <code>screenshots/</code>, and the activity will be logged in the <code>activity.log</code> file.</li>
    <li><code>CHECK_INTERVAL</code>: The interval in seconds at which the screen is checked for changes. Default is 2 seconds.</li>
    <li><code>INACTIVITY_THRESHOLD</code>: The time in seconds of screen inactivity before turning off the monitors. Default is 180 seconds (3 minutes).</li>
    <li><code>TASKBAR_HEIGHT</code>: Approximate taskbar height in pixels to avoid capturing the clock change. Adjust if needed. Default is 40 pixels.</li>
</ul>    
<h2>🛠️ Installation & Usage</h2>
<ol>
    <li>Clone this repository:</li>
    <li>Run the script:</li>
    <pre>python main.py</pre>
</ol>    
<h2>📝 Running on Windows Startup</h2>
<p>To run this script automatically when Windows starts:</p>
<ol>
    <li>Create a shortcut leading to <code>auto_start.vbs</code></li>
    <li>Press <code>Win + R</code> and type <code>shell:startup</code>, then press <code>Enter</code>.</li>
    <li>Place the created shortcut in the startup folder</li>
    <li>Restart your computer, and it will run automatically!</li>
</ol>    
<h2>📜 License</h2>
<p>This project is licensed under the MIT License.</p>
