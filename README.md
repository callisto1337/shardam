## `/reservations/`
  - **method POST**

    - Request:
      - name - name to make reservation under
      - phone - contact phone
      - guests - number of guests
      - address - address id

    - Response:
      - `OK` for success reservation
      - `FAIL` in case any error happened
