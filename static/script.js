async function loadLessons() {
    const response = await fetch("/api/lessons");
    const lessons = await response.json();

    document.getElementById("lessons").innerHTML =
        lessons.map(lesson =>
            `<div>
                <h3>${lesson.title}</h3>
                <p>${lesson.description}</p>
            </div>`
        ).join("");
}

function runPipeline() {
    const status = document.getElementById("status");

    status.innerHTML = `
        <p>✓ Build successful</p>
        <p>✓ Tests passed</p>
        <p>✓ Deployment successful</p>
    `;
}

loadLessons();