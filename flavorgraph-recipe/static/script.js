document.addEventListener("DOMContentLoaded", () => {
  const recipesDiv = document.getElementById("recipes");

  fetch("/api/recipes")
    .then(response => response.json())
    .then(data => {
      data.forEach(recipe => {
        const recipeEl = document.createElement("div");
        recipeEl.className = "recipe";

        recipeEl.innerHTML = `
          <h2>${recipe.name}</h2>
          <h4>Ingredients:</h4>
          <ul>
            ${recipe.ingredients.map(ing => `<li>${ing}</li>`).join("")}
          </ul>
        `;

        recipesDiv.appendChild(recipeEl);
      });
    })
    .catch(err => {
      recipesDiv.innerHTML = `<p style="color: red;">Error loading recipes: ${err}</p>`;
    });
});
