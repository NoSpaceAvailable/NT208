<template>
  <div class="container">
    <div class="row">
      <!-- Quick Links -->
      <div class="col-md-4 mb-4">
        <h5 class="mb-3">Quick Links</h5>
        <ul class="list-unstyled d-flex gap-3">
          <li v-for="(link, index) in links" :key="index">
            <a 
            href="#" 
            class="text-decoration-none text-dark"
            > {{ link.text }}
            </a>
          </li>
        </ul>
      </div>

      <!-- Social Media -->
      <div class="col-md-4 mb-4">
        <h5 class="mb-3">Follow Us</h5>
        <ul class="list-unstyled d-flex gap-3">
          <li>
            <a href="#" class="text-decoration-none text-dark">
              <i class="fab fa-facebook fa-2x"></i>
            </a>
          </li>
          <li>
            <a href="#" class="text-decoration-none text-dark">
              <i class="fab fa-twitter fa-2x"></i>
            </a>
          </li>
          <li>
            <a href="#" class="text-decoration-none text-dark">
              <i class="fab fa-instagram fa-2x"></i>
            </a>
          </li>
          <li>
            <a href="#" class="text-decoration-none text-dark">
              <i class="fab fa-linkedin fa-2x"></i>
            </a>
          </li>
        </ul>
      </div>

      <!-- Newsletter -->
      <div class="col-md-4 mb-4">
        <h5 class="mb-3">Subscribe to Our Newsletter</h5>
        <form>
          <div class="input-group">
            <input
              type="email"
              class="form-control"
              placeholder="Enter your email"
              aria-label="Email"
            />
            <button class="btn btn-primary" type="submit">Subscribe</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Copyright Notice -->
    <div class="text-center mt-4">
      <p class="mb-0">&copy; 2025 Almacenar. All rights reserved.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      links: [
        { text: "Home" },
        { text: "Community" },
        { text: "Marketplace" },
        { text: "About us" },
        { text: "Support" }
      ]
    }
  }
};
</script>

<style scoped>
.footer {
  background-color: #f8f9fa; /* Light gray background */
  border-top: 1px solid #e9ecef; /* Add a subtle border on top */
}

.footer h5 {
  color: #333; /* Dark gray heading */
  font-weight: 600; /* Bold heading */
}

.footer a {
  color: #333; /* Dark gray links */
  transition: color 0.3s ease; /* Smooth color transition */
}

.footer a:hover {
  color: #007bff; /* Blue color on hover */
}

.footer .form-control {
  border-radius: 0; /* Remove input border radius */
}

.footer .btn {
  border-radius: 0; /* Remove button border radius */
}

.footer .text-center {
  color: #666; /* Light gray copyright text */
}
</style>