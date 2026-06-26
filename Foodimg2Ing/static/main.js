
const wrapper = document.querySelector(".wrapper");
const fileName = document.querySelector(".file-name");
const defaultBtn = document.querySelector("#default-btn");
const customBtn = document.querySelector("#custom-btn");
const cancelBtn = document.querySelector("#cancel-btn i");
const img = document.querySelector("#foodimage");
const imgform=document.querySelector("#foodimgform");
let regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;

function defaultBtnActive(){
    defaultBtn.click();    
}
defaultBtn.addEventListener("change", function(){
    const file = this.files[0];
    if(file){
    const reader = new FileReader();
    reader.onload = function(){
        const result = reader.result;
        if (img) {
            img.src = result;
        }
        console.log(result)
        if (wrapper) {
            wrapper.classList.add("active");
        }
        document.getElementById("info").style.display = "none";
        document.getElementById("loading").style.display = "block";
        imgform.submit();
        
    }
    cancelBtn.addEventListener("click", function(){
        img.src = "";
        wrapper.classList.remove("active");
        window.location.href = "";
        
    })
    
    reader.readAsDataURL(file);
    }
    if(this.value){
    let valueStore = this.value.match(regExp);
    fileName.textContent = valueStore;
    
    }
});

function myFunctab1() {
    document.getElementById("tab2").style.display = "none";
    document.getElementById("tab1").style.display = "block";
    document.getElementById("tabbtn2").className="nav-link"
    document.getElementById("tabbtn1").className="nav-link active"
    
    
}

function myFunctab2() {
    document.getElementById("tab1").style.display = "none";
    document.getElementById("tab2").style.display = "block";
    document.getElementById("tabbtn1").className="nav-link"
    document.getElementById("tabbtn2").className="nav-link active"
}

function select(filename){
    img.src = "/static/images/"+filename
    wrapper.classList.add("active");
    document.getElementById("info").style.display = "none";
    document.getElementById("loading").style.display = "block";
    document.getElementById("close").click()
}

async function askQuestion() {

    const question =
        document.getElementById("question").value;

    const formData = new FormData();

    formData.append("question", question);

    const response =
        await fetch("/ask", {
            method: "POST",
            body: formData
        });

    const data = await response.json();

    document.getElementById("answer-box").innerHTML = marked.parse(data.answer);
}

function createMacroChart(canvasId) {

    const canvas = document.getElementById(canvasId);

    if (!canvas) return;

    const protein = Number(canvas.dataset.protein);
    const carbs = Number(canvas.dataset.carbs);
    const fat = Number(canvas.dataset.fat);
    const calories = Number(canvas.dataset.calories);

    const proteinCalories = protein * 4;
    const carbCalories = carbs * 4;
    const fatCalories = fat * 9;

    new Chart(canvas, {

        type: "doughnut",

        data: {

            labels: [
                "Protein",
                "Carbs",
                "Fat"
            ],

            datasets: [{

                data: [
                    proteinCalories,
                    carbCalories,
                    fatCalories
                ],

                backgroundColor: [
                    "#22c55e",
                    "#3b82f6",
                    "#f59e0b"
                ],

                borderColor: "#1f2937",

                borderWidth: 4,

                hoverOffset: 15

            }]

        },

        plugins: [{

            id: "centerText",

            beforeDraw(chart) {

                const {ctx} = chart;

                ctx.save();

                ctx.textAlign = "center";
                ctx.textBaseline = "middle";

                ctx.fillStyle = "#ffffff";
                ctx.font = "bold 34px Arial";

                ctx.fillText(
                    calories,
                    chart.width / 2,
                    chart.height / 2 - 12
                );

                ctx.fillStyle = "#9ca3af";
                ctx.font = "18px Arial";

                ctx.fillText(
                    "kcal",
                    chart.width / 2,
                    chart.height / 2 + 18
                );

                ctx.restore();

            }

        }],

        options: {

            responsive: true,

            maintainAspectRatio: false,

            cutout: "65%",

            animation: {

                animateRotate: true,

                duration: 1200

            },

            plugins: {

                legend: {

                    display: false

                }

            }

        }

    });

}

window.addEventListener("load", function () {

    createMacroChart("macroChart1");
    createMacroChart("macroChart2");

});