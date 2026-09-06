# PREDICTION — node split of the entrant correlation pieces on the class rows (COMPARE-DROW candidate ii). Written BEFORE any run. s30.
# Object: at the f=1 neutral SCF (drow_p path, SUBCELL=1, SIC_NOCLAMP=1), split at r_node = the entrant's OUTERMOST radial node: Q_in (entrant charge
# r < r_node), B_in = -q ∫_{r<r_node} P_e² eps_c(P_e²/w,0), A_in = ∫_{r<r_node}[n eps_c(n) - n_core eps_c(n_core)] (frozen, core = n - n_e), same for _out.
# Sc 3d is nodeless: r_node undefined, all _in = 0 by construction (control, not a test). Rows: Y La Lu; Gd for record (set aside).
PQ1 Q_in on Y La Lu in [0.03, 0.20] (one node on 4d, two on 5d; the outermost is taken).
PQ2 B_in/B in [0.2, 0.6] on all three (the inner lobe is compact: |eps_c| large where the density is high, so its share exceeds its charge share).
PQ3 B_in/excess is FLAT on Y La Lu to 20 % (excess Y 0.0102 La 0.0072 Lu 0.0083 from drow_p). B_in itself in [0.002, 0.005] Ha.
PQ4 A_in/A in [0.1, 0.4] on all three.
Rule: PQ2 and PQ3 held -> the inner-lobe self-correlation is a class quantity commensurate with the excess (0.3-0.5x), a statable candidate for the object;
PQ3 failed -> the node is not the discriminator; refused as candidate. PQ1/PQ4 are bounds on the picture, not the decision. Thresholds CHOSEN. No constant.