import express from 'express';
import { Request, Response } from 'express';

const app = express();
const port = 5000;

app.get('/', (_req: Request, res: Response) => {
    res.send('Hello World!');
});

app.listen(port, () => {
    return console.log(`Express is listening at http://localhost:${port}`);
});
