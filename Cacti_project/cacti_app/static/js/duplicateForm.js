function duplicateThisForm() {
    var count = 0;

    $('#add').click(function() {
        var source = $('form:first');
        var clone = source.clone();

        clone.find(':input').attr('id', function(i, val) {
            return val + count;
        });

        clone.find(':input').attr('name', function(i, val) {
            return val + count;
        });

        clone.insertBefore(this);
        count++;
    });
});
