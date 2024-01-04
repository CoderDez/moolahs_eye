document.addEventListener("DOMContentLoaded", function() {
    var tableRows = document.querySelectorAll(".budget-table-row");
    console.log(tableRows)

    tableRows.forEach(function(row) {
        row.addEventListener("click", function() {
            var url = this.getAttribute("data-href");
            if (url) {
                window.location.href = url;
            }
        });
    });
})
