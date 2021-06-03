## 0.1.1 / 03-06-2021
  * icon working (bundled)

## 0.1.0 / 03-06-2021
  * version 1 working for telegram, whatsapp and messenger




## Examples
## 0.6.1 / 2020-06-28
  * Support Uint8Array-s directly when decoding (#246, by @gyzerok)
  * Unify package.json version ranges to be strictly semver-compatible (#241)
  * Fix minor issue in UTF-32 decoder's endianness detection code.


## 0.6.0 / 2020-06-08
  * Updated 'gb18030' encoding to :2005 edition (see https://github.com/whatwg/encoding/issues/22).
  * Removed `iconv.extendNodeEncodings()` mechanism. It was deprecated 5 years ago and didn't work 
    in recent Node versions.
  * Reworked Streaming API behavior in browser environments to fix #204. Streaming API will be 
    excluded by default in browser packs, saving ~100Kb bundle size, unless enabled explicitly using 
    `iconv.enableStreamingAPI(require('stream'))`.
  * Updates to development environment & tests:
    * Added ./test/webpack private package to test complex new use cases that need custom environment. 
      It's tested as a separate job in Travis CI.
    * Updated generation code for the new EUC-KR index file format from Encoding Standard.
    * Removed Buffer() constructor in tests (#197 by @gabrielschulhof).