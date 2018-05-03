$(document).ready(function () {
    $("#sidenav").sideNav();

    $(".dropdown-button").dropdown();
    $('.dropdown-button').dropdown({
        hover: true, // Activate on hover
        belowOrigin: true, // Displays dropdown below the button
        alignment: 'left', // Displays dropdown with edge aligned to the left of button
    });
    loadInfo()
});

function loadInfo() {
    console.log(results[0]['id'])
    
    for (var i = 0; i < results.length; i++) {
        if (i % 2 === 0) {
            var row = document.createElement('div');
            row.className = "row";
            row.id = "content-row-" + i / 2;

            $('#content-team-container').append(row);
        }
        member = results[i];

        var container = document.createElement('div');
        container.className = "member-container col s12 m6";

        var card = document.createElement('div')
        card.className = "card blue-grey darken-1";

        container.appendChild(card);

        var card_content = document.createElement('div')
        card_content.className = "card-content white-text";

        var title = document.createElement('span');
        title.className = "card-title";
        title.innerText = member.title;

        card_content.appendChild(title);

        var description = document.createElement('p');
        // description.className = "member-name";
        description.innerText = member.description;

        card_content.appendChild(description);

        card.appendChild(card_content);

        console.log(container.innerHTML);

        $('#content-row-' + parseInt(i / 2)).append(container);
    }
}