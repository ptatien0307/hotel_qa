import "i18next";
import { defaultNS } from "../locales/i18n";
import ns1 from "../locales/vi/ns1.json";
import ns2 from "../locales/vi/ns2.json";
declare module "i18next" {
    interface CustomTypeOptions {
        defaultNS: defaultNS;
        resources: {
            ns1: typeof ns1;
            ns2: typeof ns2;
        };
    }
}
