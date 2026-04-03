import { readFileSync } from 'fs';
import { parse } from 'csv-parser';

const parseCsv = (filePath) => {
  return new Promise((resolve, reject) => {
    const csvData = [];
    const csvStream = readFileSync(filePath, 'utf8').split('\n');
    csvStream.forEach((row) => {
      csvData.push(row.split(','));
    });
    resolve(csvData);
  });
};

export default parseCsv;