let GeoCountryCode = "US";

if (typeof $argument != "undefined") {
    let arg = Object.fromEntries($argument.split("&").map((item) => item.split("=")));
    console.log(JSON.stringify(arg));
    GeoCountryCode = arg.GeoCountryCode;
};

const url = $request.url;
var body = $response.body;

const path1 = "/pep/gcc";

if (url.indexOf(path1) != -1) {
    let obj = body;
    obj = GeoCountryCode;
    body = obj;
};

$done({ body });