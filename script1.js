function submitNotice() {

    // Save notice using fetch()

    fetch("/add_notice", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: document.getElementById("title").value,
            content: document.getElementById("content").value
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        window.location.href = "/dashboard";
    });

}