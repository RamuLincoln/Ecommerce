let carts = document.querySelectorAll('.add-cart');
let products = [
    {
        name: 'chair',
        price: 250,
        incart: 0
    },
    {
        name: 'dtable',
        price: 230,
        incart: 0
    },
    {
        name: 'ctable',
        price: 200,
        incart: 0
    },
    {
        name: 'New table',
        price: 250,
        incart: 0
    },
    {
        name: 'chair',
        price: 250,
        incart: 0
    },
    {
        name: 'dtable',
        price: 230,
        incart: 0
    },
    {
        name: 'ctable',
        price: 200,
        incart: 0
    },
    {
        name: 'New table',
        price: 225,
        incart: 0
    },

]
for(let i=0;i<carts.length;i++) {
    carts[i].addEventListener('click',() => {
        cartnumbers(products[i]);
        totalcost(products[i])
    })
}

function cartnumbers(product) {
    let productnumbers = localStorage.getItem('cartnumbers');
    productnumbers = parseInt(productnumbers);
    if(productnumbers) {
        localStorage.setItem('cartnumbers', productnumbers+1)
        document.querySelector('.icons sp').textContent = productnumbers + 1;
    }else {
        localStorage.setItem('cartnumbers', 1);
        document.querySelector('.icons sp').textContent = 1;
    }

    setItems(product);
}
function setItems(product) {
    let cartItems = localStorage.getItem('productsincart');
    cartItems = JSON.parse(cartItems);
    if(cartItems != null) {
        
        if (cartItems[product.name] == undefined) {
            cartItems = {
                ...cartItems,
                [product.name]: product
            }
        }
        cartItems[product.name].incart += 1;
    }else {
        product.incart = 1;
        cartItems = {
            [product.name]: product
        }
    }
    localStorage.setItem("productsincart", JSON.stringify(cartItems) )
}

function onload() {
    let productnumbers = localStorage.getItem('cartnumbers');
    if (productnumbers) {
        document.querySelector('.icons sp').textContent = productnumbers;
    }
}

function totalcost(product) {
    //console.log("price is ", product.price);
    let cartcost = localStorage.getItem('totalcost');
    console.log("cardcost is ", cartcost);

    if (cartcost != null) {
        cartcost = parseInt(cartcost);
        console.log(cartcost);
        console.log(product.price)
        localStorage.setItem("totalcost", cartcost + product.price);
    }else {
        localStorage.setItem("totalcost", product.price);
    }

    
}
function removeItemFromCart(itemId) {
    alert("do you want to remove this : ")
    $('div').remove('#product'+itemId);
}

function displayCart() {
    let cartItems = localStorage.getItem("productsincart");
    cartItems = JSON.parse(cartItems);
    let productcontainer = document.querySelector(".products");
    let cartcost = localStorage.getItem('totalcost');
    let itemCount = 0;

    if (cartItems && productcontainer) {
        productcontainer.innerHTML = '';
        Object.values(cartItems).map(item => {
            itemCount += 1;
            productcontainer.innerHTML += `
            <div class="product" id="product` + itemCount + `">
                <button type="button" class="fa fa-window-close" onclick="removeItemFromCart(` + itemCount + `);"></button>
                <img src="static/images/${item.name}.jpeg">
                <sp>${item.name}</sp>
                <sp>$${item.price},00</sp>
                <button class="fa fa-minus-circle"></button>
                <sp>${item.incart}</sp>
                <button class="fa fa-plus-circle"></button>
                $${item.incart * item.price},00
            </div>
            `;
        });
        productcontainer.innerHTML += `
            <div class = "totalcontainer">
                <h1 class = "totaltitle">
                    total
                <h1>
                <h1 class = "total">
                    $${cartcost},00
                <h1>
            `;
    }
    
}

onload()
displayCart()