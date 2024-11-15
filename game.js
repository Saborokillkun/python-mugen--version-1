var Module = {
    // Configuration for the WebAssembly module
    totalDependencies: 0,
    preRun: [],
    postRun: [],
    
    // Handle the initialization of the game
    onRuntimeInitialized: function() {
        console.log("Game is ready!");
        startGame();
    },

    // Custom function to start the game
    startGame: function() {
        // Create and set up the canvas
        const canvas = document.getElementById("game-canvas");
        canvas.width = 1900;
        canvas.height = 950;

        // Start the game loop
        gameLoop();
    },

    // Game loop function to update the game and render each frame
    gameLoop: function() {
        // Call the Python code in the WebAssembly module to update and render
        Module._game_update();  // This is where your Python game logic gets called
        
        // Request the next frame (for continuous game loop)
        requestAnimationFrame(Module.gameLoop);
    }
};

// Load the WebAssembly file (game.wasm)
function loadWASM() {
    var script = document.createElement('script');
    script.src = "game.js";
    script.onload = function() {
        Module.onRuntimeInitialized();
    };
    document.body.appendChild(script);
}

// Initialize the game on page load
window.onload = function() {
    loadWASM();
};
