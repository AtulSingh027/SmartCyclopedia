let TopicContainer = document.getElementById("TopicContainer");

// Extract `tpk` from URL
const params = new URLSearchParams(window.location.search);
const tpk = params.get("id"); // Assuming `id` is used in the query string

async function TopicData() {
    try {
        const res = await axios.get(`http://127.0.0.1:8000/apiTopic/Topicspage/${tpk}/`);
        const data = res.data;
        console.log(data); // Debugging: Inspect API response
        DisplayData(data);
    } catch (error) {
        console.error("Error fetching topic data:", error);
        TopicContainer.innerHTML = "<p>Unable to load topics. Please try again later.</p>";
    }
}

function DisplayData(data) {
    TopicContainer.innerHTML = "";
    if (data.length === 0) {
        TopicContainer.innerHTML = "<p>No topics found for this chapter.</p>";
        return;
    }

    data.forEach((element) => {
        TopicContainer.innerHTML += `
            <div class="SubjectCard">
                <h2>🔢 ${element.topic}</h2>
                <img src="http://127.0.0.1:8000${element.image}" class="SubjectPoster" alt="Topic">
                <p>${element.description}</p>
                <div class="Btn">
                    <a href="/FrontEnd/Feed/Gemini/Gemini.html">
                        <button dataid="${element.tid}" class="card-button cs-button">Go to ai</button>
                    </a>
                </div>
            </div>
        `;
    });
}

TopicData();
