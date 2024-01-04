document.addEventListener('DOMContentLoaded', function () {
    var chartCanvas = document.getElementById('chart');
    var labels = JSON.parse(chartCanvas.getAttribute('data-labels'));
    var costs = JSON.parse(chartCanvas.getAttribute('data-costs'));

    var ctx = chartCanvas.getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                label: 'Costs',
                data: costs,
                borderWidth: 1
            }]
        },
        options: {
            legend: {
                position: 'left'
            }        
        }
    });
});
