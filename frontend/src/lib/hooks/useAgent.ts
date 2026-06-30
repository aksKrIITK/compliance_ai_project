export function useAgent() {
  return { send: async (msg: string) => msg };
}
