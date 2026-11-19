`timescale 1ns / 1ps

module fir #(
    parameter int DW = 16,
    parameter int CW = 16,
    parameter int NTAPS = 8,
    parameter int FRAC = 15
) (
    input logic clk,
    input logic rst_n,
    input logic signed [DW -1:0] x,
    input logic signed [CW -1:0] h [NTAPS],
    output logic signed [DW -1:0] y
);
    localparam int MAXV = 2**(DW-1) - 1; // 32767
    localparam int MINV = -(2**(DW-1)); // -32768
    localparam int ACCW = DW + CW + $clog2(NTAPS);
    logic signed [ACCW -1:0] acc;
    logic signed [ACCW-1:0] rounded;
    logic signed [DW -1:0] window [NTAPS];
    logic signed [DW -1:0] y_next;

    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            window <= '{default: '0};
            y <= '0;
        end else begin
            for (int i = 0; i < NTAPS -1; i++) begin
                window[i+1] <= window[i];
            end
            window[0] <= x;
            y <= y_next;
        end
    end

    always_comb begin
        acc = '0;
        for (int i = 0; i < NTAPS; i++) begin
            acc = acc + window[i]*h[i];
        end
        rounded = (acc + 2**(FRAC-1)) >>> FRAC;
        if (rounded > MAXV) y_next = DW'(MAXV);
        else if (rounded < MINV) y_next = DW'(MINV);
        else y_next = rounded[DW-1:0];
    end

endmodule : fir




