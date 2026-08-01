// =======================================
// ABC BANK ANALYTICS DASHBOARD
// =======================================

// Wait until the page loads

document.addEventListener("DOMContentLoaded", function () {

    // -----------------------------
    // Sentiment Pie Chart
    // -----------------------------

    const sentimentCanvas =
        document.getElementById("sentimentChart");

    if (sentimentCanvas) {

        new Chart(sentimentCanvas, {

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
                    ]

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

    }

    // -----------------------------
    // Language Chart
    // -----------------------------

    const languageCanvas =
        document.getElementById("languageChart");

    if (languageCanvas) {

        new Chart(languageCanvas, {

            type: "bar",

            data: {

                labels: [

                    "English",

                    "Hausa"

                ],

                datasets: [{

                    label: "Number of Chats",

                    data: [

                        englishChats,

                        hausaChats

                    ]

                }]

            },

            options: {

                responsive: true,

                scales: {

                    y: {

                        beginAtZero: true

                    }

                }

            }

        });

    }

    // -----------------------------
    // Intent Distribution
    // -----------------------------

    const intentCanvas =
        document.getElementById("intentChart");

    if (intentCanvas) {

        new Chart(intentCanvas, {

            type: "bar",

            data: {

                labels: intentLabels,

                datasets: [{

                    label: "Requests",

                    data: intentTotals

                }]

            },

            options: {

                responsive: true,

                scales: {

                    y: {

                        beginAtZero: true

                    }

                }

            }

        });

    }

});