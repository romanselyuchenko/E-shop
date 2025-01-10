document.addEventListener('DOMContentLoaded', () => {
    fetch('/products')
        .then(response => response.json())
        .then(products => {
            const productGrid = document.getElementById('product-grid');
            const productCount = document.getElementById('product-count');

            productCount.textContent = products.length;

            products.forEach(product => {
                const productDiv = document.createElement('div');
                productDiv.classList.add('product');
                productDiv.innerHTML = `
                    <img src="${product[3]}" alt="${product[1]}">
                    <h3>${product[1]}</h3>
                    <p>Цена: ${product[2]}₴</p>
                `;
                productGrid.appendChild(productDiv);
            });
        })
        .catch(error => console.error('Ошибка:', error));
});
