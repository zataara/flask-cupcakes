const BASE_URL = 'http:/localhost:5000/api';




function generateCupcakeHTML(cupcake) {
    return `
        <div data-cupcake-id=${cupcake.id}>
            <li>
                ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
            </li>
            <img class='Cupcake-img'
                    src='${cupcake.image}'
                    alt='(no image provided)'></img>
        </div>
        `;
}


