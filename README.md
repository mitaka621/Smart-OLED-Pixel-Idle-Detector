 <h1>🖥️ OLED Screen Saver</h1>
    <h2>💡 Why This is Better Than Windows' Built-in Sleep/Screen Off Function</h2>
    <ul>
       <li><strong>Perfect for Watching Movies:</strong> Unlike idle timers, this detects actual screen changes, so it won't turn off while watching videos.</li>
        <li><strong>Customizable Detection:</strong> You can adjust the time before turning off by changing the constans</li>       
        <li><strong>Extends OLED Lifespan:</strong> Specifically designed to prevent OLED burn-in, unlike Windows' generic sleep function.</li>
    </ul>
    <h2>🚀 Features</h2>
    <ul>
        <li>Monitors pixel changes on the screen.</li>
        <li>Turns off the monitor if no changes occur for a set time.</li>
        <li>Wakes up on mouse movement or keyboard input.</li>
        <li>Runs in the background efficiently.</li>
    </ul>   
    <h2>📦 Requirements</h2>
    <p>Ensure you have the following installed:</p>
    <pre>pip install mss pillow numpy</pre>    
    <h2>🛠️ Installation & Usage</h2>
    <ol>
        <li>Clone this repository:</li>
        <li>Run the script:</li>
        <pre>python main.py</pre>
    </ol>    
    <h2>📝 Running on Windows Startup</h2>
    <p>To run this script automatically when Windows starts:</p>
    <ol>
        <li>Press <code>Win + R</code> and type <code>shell:startup</code>, then press <code>Enter</code>.</li>
        <li>Copy the full path of <code>main.py</code>.</li>
        <li>Create a new text file and add the following:</li>
        <pre>        Set WshShell = CreateObject("WScript.Shell")
        WshShell.Run "python ""C:\path\to\main.py""", 0, False</pre>
        <li>Save the file as <code>oled_saver.vbs</code> and place it in the Startup folder.</li>
        <li>Restart your computer, and it will run automatically!</li>
    </ol>    
    <h2>📜 License</h2>
    <p>This project is licensed under the MIT License.</p>
