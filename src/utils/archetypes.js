// src/utils/archetypes.js
export function getArchetype(player) {
  if ((player.apg || 0) >= 8) return "Playmaker";
  if ((player.ppg || 0) >= 28 && (player.apg || 0) < 6) return "Elite Scorer";
  if ((player.rpg || 0) >= 10 && (player.ppg || 0) < 20) return "Rim Anchor";
  if ((player.ppg || 0) >= 20 && (player.rpg || 0) >= 8) return "All-Around Big";
  if ((player.ppg || 0) >= 18 && (player.apg || 0) >= 5) return "Two-Way Engine";
  if ((player.ppg || 0) >= 15) return "Scoring Wing";
  if ((player.rpg || 0) >= 8) return "Stretch Big";
  return "Role Contributor";
}
export const archetypeColors = {
  "Playmaker":"#3b82f6", "Elite Scorer":"#ff6b2b", "Rim Anchor":"#a855f7", "All-Around Big":"#14b8a6",
  "Two-Way Engine":"#22c55e", "Scoring Wing":"#eab308", "Stretch Big":"#ec4899", "Role Contributor":"#6b7280"
};
export function archetypeStyle(player) {
  const label = player.archetype || getArchetype(player);
  return { label, color: archetypeColors[label] || "#6b7280" };
}
