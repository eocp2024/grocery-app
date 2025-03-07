import React, { useState, useEffect } from "react";

function App() {
    const [mealPlan, setMealPlan] = useState([]);
    const [groceryList, setGroceryList] = useState([]);

    useEffect(() => {
        fetch("/api/meal-planner")
            .then((response) => response.json())
            .then((data) => setMealPlan(data.meal_plan));

        fetch("/api/grocery-list")
            .then((response) => response.json())
            .then((data) => setGroceryList(data.grocery_items));
    }, []);

    return (
        <div>
            <h1>Meal Planner</h1>
            <ul>
                {mealPlan.map((meal, index) => (
                    <li key={index}>{meal}</li>
                ))}
            </ul>

            <h1>Grocery List</h1>
            <ul>
                {groceryList.map((item, index) => (
                    <li key={index}>{item.name} - {item.price}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
