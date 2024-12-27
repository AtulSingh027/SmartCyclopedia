let SubjectContainer = document.getElementById("SubjectContainer");

async function Data() {
    
        let res = await axios.get("http://127.0.0.1:8000/apiSubject/Subjectspage");
        let data = res.data; // Inspect the structure here.
        console.log(data);   // Debugging: See the exact structure of the response.
        DisplayData(data);
        // Assuming the API structure is { data: [...] }, adjust as needed.
        
}

function DisplayData(data) {
    SubjectContainer.innerHTML = "";
    data.forEach(element => {
        SubjectContainer.innerHTML += `
            <div class="SubjectCard">
                <h2>🔢 ${element.subjectname}</h2>
                <img src="http://127.0.0.1:8000${element.image}" class="SubjectPoster" alt="Subject">
                <p>${element.content}</p>
                <div class="Btn">
                    <a href = "/FrontEnd/Feed/Chapters/Chapter.html?id=${element.id}">
                    <button dataid = "${element.id}" class="card-button cs-button">View Courses</button></a>
                </div>
            </div>
        `;
    });
}

Data();
