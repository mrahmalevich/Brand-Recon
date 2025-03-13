import { createRootRoute } from "@tanstack/react-router";
import { AuthProvider } from "../components/AuthProvider";

export const Route = createRootRoute({
  component: AuthProvider,
});
