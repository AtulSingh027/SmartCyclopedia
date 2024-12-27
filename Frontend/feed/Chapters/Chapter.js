let ChapterContainer = document.getElementById("ChapterContainer");

async function Data() {
    const params = new URLSearchParams(window.location.search);
    const cpk = params.get("id"); // Default to 1 if no id is provided

    try {
        const res = await axios.get(`http://127.0.0.1:8000/apiChapter/Chapterspage/${cpk}/`);
        const data = res.data;
        console.log(data);
        DisplayData(data);
    } catch (error) {
        console.error("Error fetching data:", error);
        ChapterContainer.innerHTML = "<p>Failed to load chapters. Please try again later.</p>";
    }
}

function DisplayData(data) {
    ChapterContainer.innerHTML = "";
    data.forEach(element => {
        ChapterContainer.innerHTML += `
            <div class="SubjectCard">
                <h2>🔢 ${element.chapter}</h2>
                <img src="http://127.0.0.1:8000${element.image}" class="SubjectPoster" alt="Subject">
                <p>${element.description}</p>
                <div class="Btn">
                    <a href="/frontend/Feed/Topics/Topic.html?id=${element.id}">
                        <button dataid="${element.id}" class="card-button cs-button">View Courses</button>
                    </a>
                </div>
            </div>
        `;
    });
}

Data();
