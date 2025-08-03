Bit of a gimmick, but polls https://lovely.software/rgb for RGB color codes and sets my keyboard
to whatever color it is. Anyone can change the color of my keyboard by doing a POST request to
that endpoint with the following format:

```json
{
    "red": 127,
    "green": 127,
    "blue": 127
}
```