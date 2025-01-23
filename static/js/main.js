/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById("nav-menu"),
  navToggle = document.getElementById("nav-toggle"),
  navClose = document.getElementById("nav-close");

/*===== Menu Show =====*/
/* Validate if constant exists */
if (navToggle) {
  navToggle.addEventListener("click", () => {
    navMenu.classList.add("show-menu");
  });
}

/*===== Hide Show =====*/
/* Validate if constant exists */
if (navClose) {
  navClose.addEventListener("click", () => {
    navMenu.classList.remove("show-menu");
  });
}

/*=============== IMAGE GALLERY ===============*/
function imgGallery() {
  const mainImg = document.querySelector(".details__img"),
    smallImg = document.querySelectorAll(".details__small-img");

  smallImg.forEach((img) => {
    img.addEventListener("click", function () {
      mainImg.src = this.src;
    });
  });
}

imgGallery();

/*=============== SWIPER CATEGORIES ===============*/
let swiperCategories = new Swiper(".categories__container", {
  spaceBetween: 24,
  loop: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  breakpoints: {
    350: {
      slidesPerView: 2,
      spaceBetween: 24,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 24,
    },
    992: {
      slidesPerView: 4,
      spaceBetween: 24,
    },
    1200: {
      slidesPerView: 5,
      spaceBetween: 24,
    },
    1400: {
      slidesPerView: 6,
      spaceBetween: 24,
    },
  },
});

/*=============== SWIPER PRODUCTS ===============*/
let swiperProducts = new Swiper(".new__container", {
  spaceBetween: 24,
  loop: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  breakpoints: {
    768: {
      slidesPerView: 2,
      spaceBetween: 24,
    },
    992: {
      slidesPerView: 4,
      spaceBetween: 24,
    },
    1400: {
      slidesPerView: 4,
      spaceBetween: 24,
    },
  },
});

/*=============== PRODUCTS TABS ===============*/
const tabs = document.querySelectorAll("[data-target]"),
  tabsContents = document.querySelectorAll("[content]");

tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    const target = document.querySelector(tab.dataset.target);

    tabsContents.forEach((tabsContent) => {
      tabsContent.classList.remove("active-tab");
    });

    target.classList.add("active-tab");

    tabs.forEach((tab) => {
      tab.classList.remove("active-tab");
    });

    tab.classList.add("active-tab");
  });
});









// Select DOM Elements
const productsContainer = document.querySelector('.products__container');
const wishlistTableBody = document.querySelector('.wishlist tbody');
const cartTableBody = document.querySelector('.cart tbody');
const wishlistCounter = document.querySelector('.wishlist tbody');
const cartTableCounter = document.querySelector('.cart tbody');

// Select count elements from header
const wishlistCount = document.querySelector('a[title="Wishlist"] .count');
const cartCount = document.querySelector('a[title="Cart"] .count');

// Data storage with localStorage to persist data
let wishlist = JSON.parse(localStorage.getItem('wishlist')) || [];
let cart = JSON.parse(localStorage.getItem('cart')) || [];

const shipmentPrice = 10;

// Update localStorage and counters
function updateStorage() {
    localStorage.setItem('wishlist', JSON.stringify(wishlist));
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCounters();
}

function updateCounters() {
    if (wishlistCount) wishlistCount.textContent = wishlist.length;
    if (cartCount) cartCount.textContent = cart.length;
}

// Event delegation for product actions
document.addEventListener('click', (e) => {
    const actionBtn = e.target.closest('.action__btn');
    if (!actionBtn) return;

    const productElement = actionBtn.closest('.product__item');
    if (!productElement) return;

    const product = {
        id: Date.now().toString(), // Unique ID for each product
        name: productElement.querySelector('.product__title').textContent.trim(),
        price: productElement.querySelector('.new__price').textContent.trim(),
        image: productElement.querySelector('.product__img.default').src,
    };

    if (actionBtn.getAttribute('aria-label') === 'Add to Wishlist') {
        addToWishlist(product);
    } else if (actionBtn.classList.contains('cart__btn')) {
        addToCart(product);
    }
});

// Add to Wishlist
function addToWishlist(product) {
    if(IS_LOGGED_IN === false){
        alert('Please login to add to wishlist');
        window.location.href = '/login.html';
    }else{
        if (wishlist.some(item => item.name === product.name)) {
            alert(`The item "${product.name}" is already in the wishlist!`);
            return;
        }
        wishlist.push(product);
        updateStorage();
        renderWishlist();
    }
}

// Add to Cart
function addToCart(product) {
    if(IS_LOGGED_IN === false){
        alert('Please login to add to cart');
        window.location.href = '/login.html';
    }else{
        const existingItem = cart.find(item => item.name === product.name);
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cart.push({ ...product, quantity: 1 });
        }
        updateStorage();
        renderCart();
    }
}

// Render Wishlist
function renderWishlist() {
    if (!wishlistTableBody) return;

    if (wishlist.length === 0) {
      wishlistTableBody.innerHTML = `
          <tr>
              <td colspan="6">
                  <div class="empty-state">
                      <div class="empty-state__icon">
                          <i class="fi fi-rs-heart"></i>
                      </div>
                      <h3 class="empty-state__title">Your wishlist is empty</h3>
                      <p class="empty-state__text">Looks like you haven't added any items to your wishlist yet.</p>
                      <a href="shop.html" class="btn">
                          <i class="fi fi-rs-shopping-bag"></i>
                          Continue Shopping
                      </a>
                  </div>
              </td>
          </tr>
      `;
      return;
  }
    
    wishlistTableBody.innerHTML = wishlist.map(product => `
        <tr>
            <td>
                <img src="${product.image}" alt="${product.name}" class="table__img">
            </td>
            <td>
                <h3 class="table__title">${product.name}</h3>
            </td>
            <td>
                <span class="table__price">${product.price}</span>
            </td>
            <td>
                <span class="table__stock">In Stock</span>
            </td>
            <td>
                <button class="btn btn--sm" onclick="addProductFromWishlistToCart('${product.id}')">
                    Add to Cart
                </button>
            </td>
            <td>
                <button class="btn btn--sm" onclick="removeFromWishlist('${product.id}')">
                    <i class="fi fi-rs-trash"></i>
                </button>
            </td>
        </tr>
    `).join('');
}

// Render Cart
function renderCart() {
    if (!cartTableBody) return;

    if (cart.length === 0) {
      cartTableBody.innerHTML = `
          <tr>
              <td colspan="6">
                  <div class="empty-state">
                      <div class="empty-state__icon">
                          <i class="fi fi-rs-shopping-cart"></i>
                      </div>
                      <h3 class="empty-state__title">Your cart is empty</h3>
                      <p class="empty-state__text">Looks like you haven't added any items to your cart yet.</p>
                      <a href="shop.html" class="btn">
                          <i class="fi fi-rs-shopping-bag"></i>
                          Continue Shopping
                      </a>
                  </div>
              </td>
          </tr>
      `;
      return;
  }

    cartTableBody.innerHTML = cart.map(product => `
        <tr>
            <td>
                <img src="${product.image}" alt="${product.name}" class="table__img">
            </td>
            <td>
                <h3 class="table__title">${product.name}</h3>
            </td>
            <td>
                <span class="table__price">${product.price}</span>
            </td>
            <td>
                <input 
                    type="number" 
                    value="${product.quantity}" 
                    min="1" 
                    onchange="updateCartQuantity('${product.id}', this.value)"
                    class="quantity-input"
                >
            </td>
            <td>
              
              <span class="table__price">$${(parseFloat(product.price.replace('$', '')) * product.quantity).toFixed(2)}</span>


            </td>
            <td>
                <button class="btn btn--sm" onclick="removeFromCart('${product.id}')">
                    Remove
                </button>
            </td>
        </tr>
    `).join('');

    updateCartSummary();
}

// SubTotal Price
// function subTotalPrice(product):


// Add to Cart from Wishlist
function addProductFromWishlistToCart(productId) {
    const product = wishlist.find(item => item.id === productId);
    if (product) {
        addToCart(product);
    }
}

// Remove from Wishlist
function removeFromWishlist(productId) {
    wishlist = wishlist.filter(item => item.id !== productId);
    updateStorage();
    renderWishlist();
}

// Remove from Cart
function removeFromCart(productId) {
    cart = cart.filter(item => item.id !== productId);
    updateStorage();
    renderCart();
}

// Update Cart Quantity
function updateCartQuantity(productId, quantity) {
    const newQuantity = parseInt(quantity);
    if (newQuantity < 1) return;

    cart = cart.map(item => 
        item.id === productId 
            ? { ...item, quantity: newQuantity }
            : item
    );
    updateStorage();
    renderCart();
}

// Update Cart Summary
function updateCartSummary() {
  // Calculate cart subtotal
  const subtotal = cart.reduce((total, item) => {
      const price = parseFloat(item.price.replace('$', ''));
      return total + price * item.quantity;
  }, 0);

  // Fixed shipping cost
  const shippingCost = 10.00;
  
  // Calculate grand total
  const grandTotal = subtotal + shippingCost;

  // Select all price display elements
  const cartTotalPrices = document.querySelectorAll('.cart__total-price');
  
  // Update prices if elements exist
  if (cartTotalPrices.length === 3) {
      // Update subtotal (first element)
      cartTotalPrices[0].textContent = `$${subtotal.toFixed(2)}`;
      
      // Update shipping cost (second element)
      cartTotalPrices[1].textContent = `$${shippingCost.toFixed(2)}`;
      
      // Update grand total (third element)
      cartTotalPrices[2].textContent = `$${grandTotal.toFixed(2)}`;
  }

  // Hide/show checkout button based on cart items
  const checkoutButton = document.querySelector('.cart__total a.btn');
  if (checkoutButton) {
      checkoutButton.style.display = cart.length > 0 ? 'flex' : 'none';
  }

  // Optionally hide/show entire cart total section
  const cartTotalSection = document.querySelector('.cart__total');
  if (cartTotalSection) {
      cartTotalSection.style.display = cart.product > 0 ? 'block' : 'none';
  }
}

// Initialize the page
document.addEventListener('DOMContentLoaded', () => {
    updateCounters();
    renderWishlist();
    renderCart();
});



// Previous selectors remain the same...

// Shipping Data
const shippingRates = {
  "New York": {
      cities: {
          "Manhattan": {
              "10001": 15,
              "10002": 12,
              "default": 20
          },
          "Brooklyn": {
              "11201": 18,
              "11202": 15,
              "default": 22
          },
          "default": 25
      }
  },
  "California": {
      cities: {
          "Los Angeles": {
              "90001": 20,
              "90002": 18,
              "default": 25
          },
          "San Francisco": {
              "94101": 22,
              "94102": 20,
              "default": 28
          },
          "default": 30
      }
  },
  "default": 35
};

// Coupon Codes
const validCoupons = {
  "SAVE20": { type: "percentage", value: 20 },
  "SAVE10": { type: "percentage", value: 10 },
  "FLAT50": { type: "fixed", value: 50 },
  "FREE": { type: "shipping", value: 100 }
};

// Global variables for shipping and discount
let currentShippingCost = 10.00; // Default shipping cost
let appliedCoupon = null;

// Initialize form event listeners
document.addEventListener('DOMContentLoaded', () => {
  // Previous initialization code remains...

  // Add shipping calculator form listener
  const shippingForm = document.querySelector('.cart__shippinp form');
  if (shippingForm) {
      shippingForm.addEventListener('submit', calculateShipping);
  }

  // Add coupon form listener
  const couponForm = document.querySelector('.cart__coupon form');
  if (couponForm) {
      couponForm.addEventListener('submit', applyCoupon);
  }

  // Add shipping location datalist
  addShippingDatalist();
});

// Add datalist for shipping locations
function addShippingDatalist() {
  const stateInput = document.querySelector('input[placeholder="State / Country"]');
  const cityInput = document.querySelector('input[placeholder="City"]');
  
  if (stateInput) {
      const stateList = document.createElement('datalist');
      stateList.id = 'states';
      stateList.innerHTML = Object.keys(shippingRates)
          .filter(state => state !== 'default')
          .map(state => `<option value="${state}">`)
          .join('');
      
      stateInput.setAttribute('list', 'states');
      document.body.appendChild(stateList);
  }
}

// Calculate Shipping
function calculateShipping(e) {
  e.preventDefault();

  const state = document.querySelector('input[placeholder="State / Country"]').value;
  const city = document.querySelector('input[placeholder="City"]').value;
  const postcode = document.querySelector('input[placeholder="PostCode"]').value;

  // Get shipping cost from rates object
  const stateRates = shippingRates[state] || { cities: { default: shippingRates.default } };
  const cityRates = stateRates.cities[city] || { default: stateRates.cities.default };
  const shippingCost = cityRates[postcode] || cityRates.default;

  // Update shipping cost
  currentShippingCost = shippingCost;
  
  // Show success message
  alert(`Shipping cost updated to $${shippingCost.toFixed(2)}`);
  
  // Update cart summary
  updateCartSummary();
}

// Apply Coupon
function applyCoupon(e) {
  e.preventDefault();

  const couponInput = document.querySelector('input[placeholder="Enter Your Coupon"]');
  const couponCode = couponInput.value.trim().toUpperCase();
  const coupon = validCoupons[couponCode];

  if (!coupon) {
      alert('Invalid coupon code!');
      appliedCoupon = null;
  } else {
      appliedCoupon = { ...coupon, code: couponCode };
      alert(`Coupon ${couponCode} applied successfully!`);
  }

  // Update cart summary
  updateCartSummary();
}

// Updated Cart Summary Calculation
function updateCartSummary() {
  // Calculate subtotal
  const subtotal = cart.reduce((total, item) => {
      const price = parseFloat(item.price.replace('$', ''));
      return total + price * item.quantity;
  }, 0);

  // Calculate discount if coupon is applied
  let discount = 0;
  let shippingDiscount = 0;
  
  if (appliedCoupon) {
      switch (appliedCoupon.type) {
          case 'percentage':
              discount = (subtotal * appliedCoupon.value) / 100;
              break;
          case 'fixed':
              discount = Math.min(appliedCoupon.value, subtotal); // Don't exceed subtotal
              break;
          case 'shipping':
              shippingDiscount = (currentShippingCost * appliedCoupon.value) / 100;
              break;
      }
  }

  // Calculate final shipping cost
  const finalShippingCost = Math.max(0, currentShippingCost - shippingDiscount);

  // Calculate grand total
  const grandTotal = subtotal - discount + finalShippingCost;

  // Update display
  const cartTotalPrices = document.querySelectorAll('.cart__total-price');
  
  if (cartTotalPrices.length === 3) {
      // Update subtotal
      cartTotalPrices[0].textContent = `$${subtotal.toFixed(2)}`;
      
      // Update shipping cost
      cartTotalPrices[1].textContent = `$${finalShippingCost.toFixed(2)}`;
      
      // Update grand total
      cartTotalPrices[2].textContent = `$${grandTotal.toFixed(2)}`;
  }

  // Show applied coupon info if exists
  const couponInfo = document.querySelector('.coupon-info') || 
                    document.createElement('div');
  couponInfo.className = 'coupon-info';
  
  if (appliedCoupon && (discount > 0 || shippingDiscount > 0)) {
      couponInfo.textContent = `Coupon ${appliedCoupon.code} applied: -$${(discount + shippingDiscount).toFixed(2)}`;
      const cartTotal = document.querySelector('.cart__total-table');
      if (cartTotal && !document.querySelector('.coupon-info')) {
          cartTotal.parentNode.insertBefore(couponInfo, cartTotal.nextSibling);
      }
  } else if (couponInfo.parentNode) {
      couponInfo.remove();
  }

  // Update visibility of checkout button and cart total section
  const checkoutButton = document.querySelector('.cart__total a.btn');
  const cartTotalSection = document.querySelector('.cart__total');
  
  if (checkoutButton) {
      checkoutButton.style.display = cart.length > 0 ? 'flex' : 'none';
  }
  if (cartTotalSection) {
      cartTotalSection.style.display = cart.length > 0 ? 'block' : 'none';
  }
}