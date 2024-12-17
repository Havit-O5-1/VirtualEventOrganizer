const request = require('supertest');
const app = require('./server'); // Ensure this exports your Express app

describe('API Endpoints', () => {
  it('should return API status on root route', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toEqual(200);
    expect(res.text).toEqual('Virtual Event Organizer API is running');
  });

  it('should register a new user', async () => {
    const res = await request(app).post('/api/users/register').send({
      name: 'Test User',
      email: 'test.user@example.com',
      password: 'password123',
    });
    expect(res.statusCode).toEqual(201);
    expect(res.body.message).toEqual('User registered successfully');
  });
});


