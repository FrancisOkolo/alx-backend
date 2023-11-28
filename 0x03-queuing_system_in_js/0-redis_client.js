import redis from 'redis';

// Create a Redis client
const client = redis.createClient({
  host: '127.0.0.1', // Your Redis server address
  port: 6379,        // Your Redis server port
  // Add other configuration options if needed
});

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
  // Additional error handling can be added here
});

// Event handler for connection end
client.on('end', () => {
  console.log('Redis connection ended');
});
