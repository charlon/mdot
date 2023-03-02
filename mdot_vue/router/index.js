import { createWebHistory, createRouter } from "vue-router";

// vue-gtag-next track routing
// import { trackRouter } from "vue-gtag-next";

// page components
import LauncherApp from "../pages/home.vue";
import DevResources from "../pages/developers.vue";
import PubGuidelines from "../pages/guidelines.vue";
import ProcessOverview from "../pages/overview.vue";
import RequestAccess from "../pages/access.vue";
import SponsorAgreement from "../pages/agreement.vue";
import SponsorAgree from "../pages/agree.vue";
import SponsorDecline from "../pages/decline.vue";

const routes = [
  {
    path: "/vue",
    component: LauncherApp,
  },
  {
    path: "/developers",
    component: DevResources,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/guidelines",
    component: PubGuidelines,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/overview",
    component: ProcessOverview,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/access",
    component: RequestAccess,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/agreement",
    component: SponsorAgreement,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/agree",
    component: SponsorAgree,
    pathToRegexpOptions: { strict: true },
  },
  {
    path: "/decline",
    component: SponsorDecline,
    pathToRegexpOptions: { strict: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// vue-gtag-next router tracking
// trackRouter(router);

export default router;
