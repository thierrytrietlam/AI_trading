# Analysis Etoro tickets

## Pull data from Etoro
* Check [link API](https://api-portal.etoro.com/docs/services/5770f74d6361c8154caf902b/operations/579840e06361c81270b70474).
* Check [Etoro Trading Bot](https://github.com/Gsak3l/EToro-Trading-Bot).
* Check [finvestor](https://github.com/obendidi/finvestor).
* Check [etoro-api](https://github.com/ok24601/etoro-api).

Target 1: Track movement in Etoro investors.
* Settle API with Etoro
* Pull all information in Etoro including:
    * All symbols
    * Real time positions of investors

Target 2: Analyze markets.
* Pull data from yfinance to have stock price moves.

### Get data
Go to https://www.etoro.com/discover/screener?InternalExchangeId=9
Open HTML, then find this location <ui-layout _ngcontent-ng-c2907778674="">
Download a save as a html file.
Then run the Python script to get tickets.