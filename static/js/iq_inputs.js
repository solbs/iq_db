
$(document).ready(function () {
    var fm_options = get_options(["Mother", "Father", "Brother", "Sister", "Husband", "Wife", "Son", "Daughter"]);
    console.log(fm_options);
    $('#Family_Members').selectize({
        options: fm_options,
        valueField: "value",
        sortField: "idx",
        labelField: "value",
        searchField: "value",
        delimiter: ',',
        persist: false,
        selectOnTab: true,
        create: function(input) {
            return {
                value: input,
                text: input
            }
        }
    });
});
