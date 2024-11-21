$(document).ready(function () {
    $('#submit-guess').click(function () {
        var letter = $('#guess-input').val();
        if (letter) {
            $.post('/guess', { letter: letter }, function (response) {
                if (response.game_over) {
                    window.location.href = '/game_over?status=' + response.status + '&word=' + response.word;
                } else {
                    $('#current-word').text(response.current_word.split('').join(' '));
                    $('#guesses').text(response.guesses.join(', '));
                    $('#tries-left').text(response.tries_left);
                    updateHangmanImage(response.tries_left);
                }
                $('#guess-input').val('');
            });
        }
    });

    function updateHangmanImage(tries_left) {
        var image_path = '/static/img/hangman_' + (7 - tries_left) + '.png';
        $('#hangman-image').attr('src', image_path);
    }
});
