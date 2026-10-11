// ===========================================
// ABC BANK AI DASHBOARD
// dashboard.js
// ===========================================

// ===============================
// SENTIMENT CHART
// ===============================

const sentimentCtx = document
    .getElementById("sentimentChart")
    .getContext("2d");

new Chart(sentimentCtx, {

    type: "pie",

    data: {

        labels: [

            "Positive",
            "Neutral",
            "Negative"

        ],

        datasets: [{

            data: [

                positiveChats,
                neutralChats,
                negativeChats

            ],

            backgroundColor: [

                "#198754",
                "#ffc107",
                "#dc3545"

            ],

            borderWidth: 1

        }]

    },

    options: {

        responsive: true,

        plugins: {

            legend: {

                position: "bottom"

            }

        }

    }

});


// ===============================
// LANGUAGE CHART
// ===============================

const languageCtx = document
    .getElementById("languageChart")
    .getContext("2d");

new Chart(languageCtx, {

    type: "doughnut",

    data: {

        labels: [

            "English",
            "Hausa"

        ],

        datasets: [{

            data: [

                englishChats,
                hausaChats

            ],

            backgroundColor: [

                "#0d6efd",
                "#6f42c1"

            ],

            borderWidth: 1

        }]

    },

    options: {

        responsive: true,

        plugins: {

            legend: {

                position: "bottom"

            }

        }

    }

});


// ===============================
// INTENT DISTRIBUTION
// ===============================

const intentCtx = document
    .getElementById("intentChart")
    .getContext("2d");

new Chart(intentCtx, {

    type: "bar",

    data: {

        labels: intentLabels,

        datasets: [{

            label: "Total Requests",

            data: intentTotals,

            backgroundColor: "#003366",

            borderRadius: 8

        }]

    },

    options: {

        responsive: true,

        plugins: {

            legend: {

                display: false

            }

        },

        scales: {

            y: {

                beginAtZero: true,

                ticks: {

                    precision: 0

                }

            }

        }

    }

});