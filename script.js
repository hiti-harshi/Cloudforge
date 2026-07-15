const backendURL = "http://127.0.0.1:5000";

const launchBtn = document.getElementById("launchBtn");
const destroyBtn = document.getElementById("destroyBtn");
const copyBtn = document.getElementById("copyBtn");

if (launchBtn) {

    launchBtn.addEventListener("click", launchLab);

}

if (destroyBtn) {

    destroyBtn.addEventListener("click", destroyLab);

}

if (copyBtn) {

    copyBtn.addEventListener("click", copySSH);

}


async function launchLab() {

    document.getElementById("status").innerText = "Launching Lab...";

    try {

        const response = await fetch(`${backendURL}/create-lab`);

        const data = await response.json();

        if (data.status === "success") {

            const outputs = data.outputs;
            document.getElementById("status").innerText =
               outputs.instance_state;

            document.getElementById("ip").innerText =
               outputs.public_ip;

            document.getElementById("dns").innerText =
               outputs.public_dns;

            document.getElementById("ssh").innerText =
               `ssh -i cloudforge-key.pem ubuntu@${outputs.public_ip}`;
            

        }
        else {

            alert(data.message);

        }

    }

    catch (err) {

        alert("Unable to connect to backend.");

    }

}



async function destroyLab() {

    const response = await fetch(`${backendURL}/destroy-lab`);

    const data = await response.json();

    alert(data.message);

    document.getElementById("status").innerText = "Destroyed";

    document.getElementById("ip").innerText = "-";

    document.getElementById("dns").innerText = "-";

    document.getElementById("ssh").innerText = "-";

}



function copySSH() {

    navigator.clipboard.writeText(

        document.getElementById("ssh").innerText

    );

    alert("SSH Command Copied!");

}