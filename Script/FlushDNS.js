/*
 * 作者: @Bob
 * 更新日期: 2022-09-04
 * 版本: 1.0
 * 使用: 刷新 DNS = type=cron,cronexp=00 10 * * *,script-path=https://raw.githubusercontent.com/bob-zebedy/Surge/master/Script/FlushDNS.js,script-update-interval=0 
 */

!(async () => {
    let panel = { title: "Flush DNS" },
        showServer = true,
        dnsCache;
    if (typeof $argument != "undefined") {
        let arg = Object.fromEntries($argument.split("&").map((item) => item.split("=")));
        if (arg.title) panel.title = arg.title;
        if (arg.icon) panel.icon = arg.icon;
        if (arg.color) panel["icon-color"] = arg.color;
        if (arg.server == "false") showServer = false;
    }
    if (showServer) {
        dnsCache = (await httpAPI("/v1/dns", "GET")).dnsCache;
        dnsCache = [...new Set(dnsCache.map((d) => d.server))].toString().replace(/,/g, "\n");
    }
    if ($trigger == "button") await httpAPI("/v1/dns/flush");
    let delay = ((await httpAPI("/v1/test/dns_delay")).delay * 1000).toFixed(0);
    panel.content = `DNS 延迟: ${delay}ms${dnsCache ? `\nserver:\n${dnsCache}` : ""}`;
    $done(panel);
})();

function httpAPI(path = "", method = "POST", body = null) {
    return new Promise((resolve) => {
        $httpAPI(method, path, body, (result) => {
            resolve(result);
        });
    });
}