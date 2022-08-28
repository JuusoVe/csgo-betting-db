import express from 'express';
import { Request, Response } from 'express';

const app = express();
const port = 5000;

app.get('/', (_req: Request, res: Response) => {
    const DATABASE_URI_IS_DEFINED = !process.env?.DATABASE_URI === undefined;
    res.send('DB url is defined: ' + DATABASE_URI_IS_DEFINED);
});

app.listen(port, () => {
    return console.log(`Express is listening at http://localhost:${port}`);
});
